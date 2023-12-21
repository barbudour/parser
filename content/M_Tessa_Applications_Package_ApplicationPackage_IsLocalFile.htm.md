# ApplicationPackage.IsLocalFile - метод
Возвращает значение, показывающее, содержится ли указанный хеш в
[LocalFilesHash](P_Tessa_Applications_Package_ApplicationPackage_LocalFilesHash.htm),
если содержится, то файл имеющий указанный хеш присутствует на клиенте.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsLocalFile(
    	byte[] hash
    )
VB __Копировать
     Public Function IsLocalFile ( 
    	hash As Byte()
    ) As Boolean
C++ __Копировать
     public:
    bool IsLocalFile(
    	array<unsigned char>^ hash
    )
F# __Копировать
     member IsLocalFile : 
            hash : byte[] -> bool 
#### Параметры
hash [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
    Проверяемый хеш.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Значение true? если указанный хеш содержится в
[LocalFilesHash](P_Tessa_Applications_Package_ApplicationPackage_LocalFilesHash.htm),
иначе - false.
##  __См. также
#### Ссылки
[ApplicationPackage - ](T_Tessa_Applications_Package_ApplicationPackage.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
