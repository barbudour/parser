# ICardTypePolicy.IsAllowed(String) - метод
Возвращает признак того, что выполнение методов расширения допустимо для типа
карточки с заданным именем.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool IsAllowed(
    	string cardTypeName
    )
VB __Копировать
     Function IsAllowed ( 
    	cardTypeName As String
    ) As Boolean
C++ __Копировать
     bool IsAllowed(
    	String^ cardTypeName
    )
F# __Копировать
     abstract IsAllowed : 
            cardTypeName : string -> bool 
#### Параметры
cardTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя типа карточки.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если выполнение методов расширения допустимо для типа карточки с
заданным именем; false в противном случае.
## __См. также
#### Ссылки
[ICardTypePolicy - ](T_Tessa_Cards_Extensions_ICardTypePolicy.htm)
[IsAllowed -
перегрузка](Overload_Tessa_Cards_Extensions_ICardTypePolicy_IsAllowed.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
