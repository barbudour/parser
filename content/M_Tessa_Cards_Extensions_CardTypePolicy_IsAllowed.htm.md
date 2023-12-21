# CardTypePolicy.IsAllowed(String) - метод
Возвращает признак того, что выполнение методов расширения допустимо для типа
карточки с заданным именем.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsAllowed(
    	string cardTypeName
    )
VB __Копировать
     Public Function IsAllowed ( 
    	cardTypeName As String
    ) As Boolean
C++ __Копировать
     public:
    virtual bool IsAllowed(
    	String^ cardTypeName
    ) sealed
F# __Копировать
     abstract IsAllowed : 
            cardTypeName : string -> bool 
    override IsAllowed : 
            cardTypeName : string -> bool 
#### Параметры
cardTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя типа карточки.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если выполнение методов расширения допустимо для типа карточки с
заданным именем; false в противном случае.
#### Реализации
[ICardTypePolicy.IsAllowed(String)](M_Tessa_Cards_Extensions_ICardTypePolicy_IsAllowed.htm)  
##  __См. также
#### Ссылки
[CardTypePolicy - ](T_Tessa_Cards_Extensions_CardTypePolicy.htm)
[IsAllowed -
перегрузка](Overload_Tessa_Cards_Extensions_CardTypePolicy_IsAllowed.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
