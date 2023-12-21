# FileTag - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileTag(
    	string key,
    	Dictionary<string, Object> info = null,
    	bool seal = false
    )
VB __Копировать
     Public Sub New ( 
    	key As String,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional seal As Boolean = false
    )
C++ __Копировать
     public:
    FileTag(
    	String^ key, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	bool seal = false
    )
F# __Копировать
     new : 
            key : string * 
            ?info : Dictionary<string, Object> * 
            ?seal : bool 
    (* Defaults:
            let _info = defaultArg info null
            let _seal = defaultArg seal false
    *)
    -> FileTag
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, уникально идентифицирующий тег. При сравнении ключей обычно не учитывается регистр символов.
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
    Дополнительная информация для расширений или null, если информация не требуется.
seal [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что объект защищается от изменений сразу после создания.
##  __См. также
#### Ссылки
[FileTag - ](T_Tessa_Files_FileTag.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
