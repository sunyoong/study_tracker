from django.shortcuts import render
from django.http import JsonResponse
from pymongo import MongoClient

# Create your views here.
def test_insert(request):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["testdb"]
    collection = db["people"]
    
    # 테스트용 데이터
    data = {"name":"alice", "age":25}

    # insert
    result = collection.insert_one(data)    
    
    # 응답데이터 반환
    return JsonResponse({"insert_one": str(result.inserted_id)})
