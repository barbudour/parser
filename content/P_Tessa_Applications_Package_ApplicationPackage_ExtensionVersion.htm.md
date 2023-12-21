# ApplicationPackage.ExtensionVersion - свойство
Примечание: Данный API устарел.
Gets or sets Версия расширения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [CanBeNullAttribute]
    [DataMemberAttribute(IsRequired = false)]
    [ObsoleteAttribute("Used in previous versions, serializable to old versions of TessaAppManager.")]
    public string ExtensionVersion { get; set; }
VB __Копировать
    <CanBeNullAttribute>
    <DataMemberAttribute(IsRequired := false)>
    <ObsoleteAttribute("Used in previous versions, serializable to old versions of TessaAppManager.")>
    Public Property ExtensionVersion As String
    	Get
    	Set
C++ __Копировать
     public:
    [CanBeNullAttribute]
    [DataMemberAttribute(IsRequired = false)]
    [ObsoleteAttribute(L"Used in previous versions, serializable to old versions of TessaAppManager.")]
    property String^ ExtensionVersion {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     [<CanBeNullAttribute>]
    [<DataMemberAttribute(IsRequired = false)>]
    [<ObsoleteAttribute("Used in previous versions, serializable to old versions of TessaAppManager.")>]
    member ExtensionVersion : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[ApplicationPackage - ](T_Tessa_Applications_Package_ApplicationPackage.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
