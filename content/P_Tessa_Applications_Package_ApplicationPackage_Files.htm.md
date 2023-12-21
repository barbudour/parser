# ApplicationPackage.Files - свойство
Gets or sets Список файлов
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    [DataMemberAttribute]
    public List<ApplicationPackageFile> Files { get; set; }
VB __Копировать
    <NotNullAttribute>
    <DataMemberAttribute>
    Public Property Files As List(Of ApplicationPackageFile)
    	Get
    	Set
C++ __Копировать
     public:
    [NotNullAttribute]
    [DataMemberAttribute]
    property List<ApplicationPackageFile^>^ Files {
    	List<ApplicationPackageFile^>^ get ();
    	void set (List<ApplicationPackageFile^>^ value);
    }
F# __Копировать
     [<NotNullAttribute>]
    [<DataMemberAttribute>]
    member Files : List<ApplicationPackageFile> with get, set
#### Значение свойства
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[ApplicationPackageFile](T_Tessa_Applications_Package_ApplicationPackageFile.htm)>
##  __См. также
#### Ссылки
[ApplicationPackage - ](T_Tessa_Applications_Package_ApplicationPackage.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
