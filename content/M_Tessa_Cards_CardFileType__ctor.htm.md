# CardFileType(String, String, Nullable<Guid>) - конструктор
Создаёт виртуальный тип карточки с заданными уникальным и отображаемым именем.
Свойство [CardType](P_Tessa_Cards_CardFileType_CardType.htm) созданного типа
будет равно null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileType(
    	string name,
    	string caption,
    	Guid? id = null
    )
VB __Копировать
     Public Sub New ( 
    	name As String,
    	caption As String,
    	Optional id As Guid? = Nothing
    )
C++ __Копировать
     public:
    CardFileType(
    	String^ name, 
    	String^ caption, 
    	Nullable<Guid> id = nullptr
    )
F# __Копировать
     new : 
            name : string * 
            caption : string * 
            ?id : Nullable<Guid> 
    (* Defaults:
            let _id = defaultArg id null
    *)
    -> CardFileType
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Уникальное имя типа файла в карточке.
caption [String](https://learn.microsoft.com/dotnet/api/system.string)
    Отображаемое имя типа файла в карточке.
id
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Идентификатор типа, используемый для объединения типов в группы, или null, если генерируется идентификатор по заданному имени name. 
## __См. также
#### Ссылки
[CardFileType - ](T_Tessa_Cards_CardFileType.htm)
[CardFileType - перегрузка](Overload_Tessa_Cards_CardFileType__ctor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
