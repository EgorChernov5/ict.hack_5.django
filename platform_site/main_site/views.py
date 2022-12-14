from rest_framework import generics
from .serializers import *
from rest_framework import filters
from .models import *
from rest_framework.response import Response
from django.db.models import Avg
from rest_framework.views import APIView
from statistics import mean
import numpy as np
from rest_framework.permissions import *
from rest_framework import status
from .permissions import *
from rest_framework import mixins


class DetailCVAPIView(generics.RetrieveAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
    # permission_classes = [IsAuthenticated]


class ListCVAPIView(generics.ListAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
    # permission_classes = [IsAuthenticated]


class DeleteCVAPIView(generics.RetrieveDestroyAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
    # permission_classes = [IsAuthenticated]


class UpdateCVAPIView(generics.RetrieveUpdateAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
    # permission_classes = [IsAuthenticated]


class CreateCVAPIView(generics.CreateAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
    permission_classes = [IsAuthenticated]


class DeleteCompanyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class UpdateCompanyAPIView(generics.RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CreateCompanyAPIView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CreateCompanySerializer
    permission_classes = [IsAuthenticated]


class AllCompanyAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = AllCompanySerializer
    permission_classes = [AllowAny]


class CompanyAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]


class AllDetailCompanyAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class DetailCompanyProjectsAPIView(generics.RetrieveAPIView):
    queryset = CompanyProjects.objects.all()
    serializer_class = CompanyProjectsSerializer


class CreateStudentAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = CreateStudentsSerializer
    permission_classes = [IsAuthenticated]


class CompanyProjectsAPIView(generics.ListAPIView):
    queryset = CompanyProjects.objects.all()
    serializer_class = CompanyProjectsSerializer


class AllStudentsAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = AllStudentsSerializer
    permission_classes = [AllowAny]


class AdminStudentsAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
    # permission_classes = [IsAuthenticated]


class GetStudentsByRateAPIView(generics.ListAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["work_speed", "communication", "tech_part"]


# permission_classes = [IsAuthenticated]


class GetMeanScore(APIView):
    def get(self, request):
        mean_work_speed = Rate.objects.values("identification_student") \
            .annotate(mean_speed=Avg("work_speed"),
                      mean_communcation=Avg("communication"),
                      mean_tech_part=Avg("tech_part"))

        for i in range(len(mean_work_speed)):
            dic = mean_work_speed[i]
            speed = dic["mean_speed"]
            communcation = dic["mean_communcation"]
            tech_part = dic["mean_tech_part"]
            mean_score = mean([speed, communcation, tech_part])
            dic["mean_score"] = np.around(float(mean_score), 2)

        return Response(mean_work_speed)


class GetStudentsByTagAPIViews(generics.ListAPIView):
    serializer_class = SortedStudentsSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        required_name_tags = self.request.query_params.getlist('tags[]')
        required_tags = []
        for required_name_tag in required_name_tags:
            try:
                required_tags.append(Tags.objects.get(name_tag=required_name_tag).pk)
            except:
                continue

        tags = []
        if len(required_tags):
            queryset = Student.objects.filter(tags=required_tags[0])
            for tag in tags:
                queryset |= Student.objects.filter(tags=tag)

            if len(queryset):
                return queryset.order_by("-mean_rate")

        return Student.objects.none()


class DetailStudentsAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthenticated]


class AllDetailStudentsAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = AllStudentsSerializer
    permission_classes = [AllowAny]


class GetTagsAPIView(generics.ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class UpdateProjectCompany(generics.RetrieveUpdateAPIView):
    queryset = CompanyProjects.objects.all()
    serializer_class = CompanyProjectsSerializer


class DeleteProjectCompany(generics.RetrieveDestroyAPIView):
    queryset = CompanyProjects.objects.all()
    serializer_class = CompanyProjectsSerializer


class CreateProjectCompany(generics.CreateAPIView):
    queryset = CompanyProjects.objects.all()
    serializer_class = CompanyProjectsSerializer
    permission_classes = [IsAuthenticated]


class CreateCompanyBid(generics.CreateAPIView):
    queryset = CompanyBid.objects.all()
    serializer_class = CompanyBidSerializer
    # permission_classes = [IsAuthenticated]


class UpdateCompanyBid(generics.UpdateAPIView):
    queryset = CompanyBid.objects.all()
    serializer_class = CompanyBidUpdateSerializer
    # permission_classes = [IsAuthenticated]

class CreateStudentBid(generics.CreateAPIView):
    queryset = StudentBid.objects.all()
    serializer_class = StudentBidSerializer
    # permission_classes = [IsAuthenticated]

class UpdateStudentBid(generics.UpdateAPIView):
    queryset = StudentBid.objects.all()
    serializer_class = StudentBidSerializer
    # permission_classes = [IsAuthenticated]