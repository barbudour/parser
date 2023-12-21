# CardValidatorType(Guid, String, CardValidationMode[], CardInstanceType[]) -
конструктор
Создаёт экземпляр типа с заданными идентификатором и именем.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardValidatorType(
    	Guid id,
    	string name,
    	CardValidationMode[] allowedValidationModes,
    	CardInstanceType[] allowedInstanceTypes = null
    )
VB __Копировать
     Public Sub New ( 
    	id As Guid,
    	name As String,
    	allowedValidationModes As CardValidationMode(),
    	Optional allowedInstanceTypes As CardInstanceType() = Nothing
    )
C++ __Копировать
     public:
    CardValidatorType(
    	Guid id, 
    	String^ name, 
    	array<CardValidationMode>^ allowedValidationModes, 
    	array<CardInstanceType>^ allowedInstanceTypes = nullptr
    )
F# __Копировать
     new : 
            id : Guid * 
            name : string * 
            allowedValidationModes : CardValidationMode[] * 
            ?allowedInstanceTypes : CardInstanceType[] 
    (* Defaults:
            let _allowedInstanceTypes = defaultArg allowedInstanceTypes null
    *)
    -> CardValidatorType
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа.
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Отображаемое имя типа.
allowedValidationModes
[CardValidationMode](T_Tessa_Cards_Validation_CardValidationMode.htm)[]
     Способы выполнения валидации, для которых разрешено использование валидатора. Если задано null или пустой массив, то считается, что для валидатора разрешены типы [Card](T_Tessa_Cards_Validation_CardValidationMode.htm) и [Task](T_Tessa_Cards_Validation_CardValidationMode.htm). 
allowedInstanceTypes [CardInstanceType](T_Tessa_Cards_CardInstanceType.htm)[]
(Optional)
     Типы экземпляров карточек, для которых разрешено использование валидатора. Если задано null или пустой массив, то считается, что для валидатора разрешены все типы экземпляров. 
## __См. также
#### Ссылки
[CardValidatorType - ](T_Tessa_Cards_CardValidatorType.htm)
[CardValidatorType -
перегрузка](Overload_Tessa_Cards_CardValidatorType__ctor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
