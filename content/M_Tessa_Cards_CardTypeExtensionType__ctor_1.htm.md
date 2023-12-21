# CardTypeExtensionType(Guid, String, CardInstanceType[]) - конструктор
Создаёт экземпляр типа с заданными идентификатором и именем.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTypeExtensionType(
    	Guid id,
    	string name,
    	CardInstanceType[] allowedInstanceTypes = null
    )
VB __Копировать
     Public Sub New ( 
    	id As Guid,
    	name As String,
    	Optional allowedInstanceTypes As CardInstanceType() = Nothing
    )
C++ __Копировать
     public:
    CardTypeExtensionType(
    	Guid id, 
    	String^ name, 
    	array<CardInstanceType>^ allowedInstanceTypes = nullptr
    )
F# __Копировать
     new : 
            id : Guid * 
            name : string * 
            ?allowedInstanceTypes : CardInstanceType[] 
    (* Defaults:
            let _allowedInstanceTypes = defaultArg allowedInstanceTypes null
    *)
    -> CardTypeExtensionType
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа.
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Отображаемое имя типа.
allowedInstanceTypes [CardInstanceType](T_Tessa_Cards_CardInstanceType.htm)[]
(Optional)
     Типы экземпляров карточек, для которых разрешено использование этого расширения типа. Если задано null или пустой массив, то считается, что для расширения разрешены все типы экземпляров. 
## __См. также
#### Ссылки
[CardTypeExtensionType - ](T_Tessa_Cards_CardTypeExtensionType.htm)
[CardTypeExtensionType -
перегрузка](Overload_Tessa_Cards_CardTypeExtensionType__ctor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
