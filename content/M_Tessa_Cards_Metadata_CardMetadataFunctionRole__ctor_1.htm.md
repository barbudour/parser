# CardMetadataFunctionRole(Guid, String, String, Boolean) - конструктор
Создаёт экземпляр класса с указанием свойств вариантов завершения.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadataFunctionRole(
    	Guid id,
    	string name,
    	string caption,
    	bool canBeDeputy = true
    )
VB __Копировать
     Public Sub New ( 
    	id As Guid,
    	name As String,
    	caption As String,
    	Optional canBeDeputy As Boolean = true
    )
C++ __Копировать
     public:
    CardMetadataFunctionRole(
    	Guid id, 
    	String^ name, 
    	String^ caption, 
    	bool canBeDeputy = true
    )
F# __Копировать
     new : 
            id : Guid * 
            name : string * 
            caption : string * 
            ?canBeDeputy : bool 
    (* Defaults:
            let _canBeDeputy = defaultArg canBeDeputy true
    *)
    -> CardMetadataFunctionRole
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор варианта завершения.
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя варианта завершения.
caption [String](https://learn.microsoft.com/dotnet/api/system.string)
    Отображаемое название для варианта завершения.
canBeDeputy [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что в функциональную роль включаются заместители.
##  __См. также
#### Ссылки
[CardMetadataFunctionRole -
](T_Tessa_Cards_Metadata_CardMetadataFunctionRole.htm)
[CardMetadataFunctionRole -
перегрузка](Overload_Tessa_Cards_Metadata_CardMetadataFunctionRole__ctor.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
