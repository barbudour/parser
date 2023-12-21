# ICardMethodPolicy<TMethod>.IsAllowed - метод
Проверяет, что заданный метод является допустимым для выполнения расширения.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool IsAllowed(
    	TMethod method
    )
VB __Копировать
     Function IsAllowed ( 
    	method As TMethod
    ) As Boolean
C++ __Копировать
     bool IsAllowed(
    	TMethod method
    )
F# __Копировать
     abstract IsAllowed : 
            method : 'TMethod -> bool 
#### Параметры
method [TMethod](T_Tessa_Cards_Extensions_ICardMethodPolicy_1.htm)
    Тип метода выполнения запроса к API карточек.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если заданный метод является допустимым для выполнения расширения; false
в противном случае.
## __См. также
#### Ссылки
[ICardMethodPolicy<TMethod> \-
](T_Tessa_Cards_Extensions_ICardMethodPolicy_1.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
