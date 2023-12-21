# ApplicationPackageFile(String, String, Guid, Int64, Byte[], Nullable<Guid>,
Nullable<Guid>, Nullable<CardFileSourceType>, PackageFileState, Boolean) -
конструктор
Initializes a new instance of the
[ApplicationPackageFile](T_Tessa_Applications_Package_ApplicationPackageFile.htm)
class. Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationPackageFile(
    	[NotNullAttribute] string name,
    	[NotNullAttribute] string fullName,
    	Guid id,
    	long size,
    	[CanBeNullAttribute] byte[] hash = null,
    	Guid? applicationId = null,
    	Guid? versionId = null,
    	CardFileSourceType? sourceTypeId = null,
    	PackageFileState state = PackageFileState.Unchanged,
    	bool isLocal = false
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> name As String,
    	<NotNullAttribute> fullName As String,
    	id As Guid,
    	size As Long,
    	<CanBeNullAttribute> Optional hash As Byte() = Nothing,
    	Optional applicationId As Guid? = Nothing,
    	Optional versionId As Guid? = Nothing,
    	Optional sourceTypeId As CardFileSourceType? = Nothing,
    	Optional state As PackageFileState = PackageFileState.Unchanged,
    	Optional isLocal As Boolean = false
    )
C++ __Копировать
     public:
    ApplicationPackageFile(
    	[NotNullAttribute] String^ name, 
    	[NotNullAttribute] String^ fullName, 
    	Guid id, 
    	long long size, 
    	[CanBeNullAttribute] array<unsigned char>^ hash = nullptr, 
    	Nullable<Guid> applicationId = nullptr, 
    	Nullable<Guid> versionId = nullptr, 
    	Nullable<CardFileSourceType> sourceTypeId = nullptr, 
    	PackageFileState state = PackageFileState::Unchanged, 
    	bool isLocal = false
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] name : string * 
            [<NotNullAttribute>] fullName : string * 
            id : Guid * 
            size : int64 * 
            [<CanBeNullAttribute>] ?hash : byte[] * 
            ?applicationId : Nullable<Guid> * 
            ?versionId : Nullable<Guid> * 
            ?sourceTypeId : Nullable<CardFileSourceType> * 
            ?state : PackageFileState * 
            ?isLocal : bool 
    (* Defaults:
            let _hash = defaultArg hash null
            let _applicationId = defaultArg applicationId null
            let _versionId = defaultArg versionId null
            let _sourceTypeId = defaultArg sourceTypeId null
            let _state = defaultArg state PackageFileState.Unchanged
            let _isLocal = defaultArg isLocal false
    *)
    -> ApplicationPackageFile
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя файла 
fullName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Полное имя файла 
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор файла 
size [Int64](https://learn.microsoft.com/dotnet/api/system.int64)
     Размер 
hash [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[] (Optional)
     Контрольная сумма 
applicationId
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Идентификатор приложения 
versionId
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Идентификатор версии 
sourceTypeId
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[CardFileSourceType](T_Tessa_Cards_CardFileSourceType.htm)>
(Optional)
     Идентификатор типа источника 
state [PackageFileState](T_Tessa_Applications_Package_PackageFileState.htm)
(Optional)
    Состояние файла
isLocal [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Значение true, если файл доступен локально, иначе - false.
##  __См. также
#### Ссылки
[ApplicationPackageFile -
](T_Tessa_Applications_Package_ApplicationPackageFile.htm)
[ApplicationPackageFile -
перегрузка](Overload_Tessa_Applications_Package_ApplicationPackageFile__ctor.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
