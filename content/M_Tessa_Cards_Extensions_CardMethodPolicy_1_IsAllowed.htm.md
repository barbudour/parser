# CardMethodPolicy<TMethod>.IsAllowed - метод
Проверяет, что заданный метод является допустимым для выполнения расширения.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsAllowed(
    	TMethod method
    )
VB __Копировать
     Public Function IsAllowed ( 
    	method As TMethod
    ) As Boolean
C++ __Копировать
     public:
    virtual bool IsAllowed(
    	TMethod method
    ) sealed
F# __Копировать
     abstract IsAllowed : 
            method : 'TMethod -> bool 
    override IsAllowed : 
            method : 'TMethod -> bool 
#### Параметры
method [TMethod](T_Tessa_Cards_Extensions_CardMethodPolicy_1.htm)
    Тип метода выполнения запроса к API карточек.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если заданный метод является допустимым для выполнения расширения; false
в противном случае.
#### Реализации
[ICardMethodPolicy<TMethod>.IsAllowed(TMethod)](M_Tessa_Cards_Extensions_ICardMethodPolicy_1_IsAllowed.htm)  
##  __См. также
#### Ссылки
[CardMethodPolicy<TMethod> \-
](T_Tessa_Cards_Extensions_CardMethodPolicy_1.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
