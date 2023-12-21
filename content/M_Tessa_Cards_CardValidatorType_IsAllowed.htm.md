# CardValidatorType.IsAllowed(CardInstanceType) - метод
Возвращает признак того, что валидатор разрешён для заданного типа экземпляра
карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsAllowed(
    	CardInstanceType instanceType
    )
VB __Копировать
     Public Function IsAllowed ( 
    	instanceType As CardInstanceType
    ) As Boolean
C++ __Копировать
     public:
    bool IsAllowed(
    	CardInstanceType instanceType
    )
F# __Копировать
     member IsAllowed : 
            instanceType : CardInstanceType -> bool 
#### Параметры
instanceType [CardInstanceType](T_Tessa_Cards_CardInstanceType.htm)
    Тип экземпляра карточки, который требуется проверить.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если валидатор разрешён для заданного типа экземпляра карточки; false в
противном случае.
## __См. также
#### Ссылки
[CardValidatorType - ](T_Tessa_Cards_CardValidatorType.htm)
[IsAllowed - перегрузка](Overload_Tessa_Cards_CardValidatorType_IsAllowed.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
