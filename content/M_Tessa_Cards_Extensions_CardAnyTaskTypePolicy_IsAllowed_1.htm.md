# CardAnyTaskTypePolicy.IsAllowed(CardType) - метод
Возвращает признак того, что выполнение методов расширения допустимо для
заданного типа задания.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsAllowed(
    	CardType taskType
    )
VB __Копировать
     Public Function IsAllowed ( 
    	taskType As CardType
    ) As Boolean
C++ __Копировать
     public:
    virtual bool IsAllowed(
    	CardType^ taskType
    ) sealed
F# __Копировать
     abstract IsAllowed : 
            taskType : CardType -> bool 
    override IsAllowed : 
            taskType : CardType -> bool 
#### Параметры
taskType [CardType](T_Tessa_Cards_CardType.htm)
    Тип задания, идентификатор или имя которого проверяются.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если выполнение методов расширения допустимо для заданного типа задания;
false в противном случае.
#### Реализации
[ICardTaskTypePolicy.IsAllowed(CardType)](M_Tessa_Cards_Extensions_ICardTaskTypePolicy_IsAllowed_1.htm)  
##  __См. также
#### Ссылки
[CardAnyTaskTypePolicy - ](T_Tessa_Cards_Extensions_CardAnyTaskTypePolicy.htm)
[IsAllowed -
перегрузка](Overload_Tessa_Cards_Extensions_CardAnyTaskTypePolicy_IsAllowed.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
