# CardFileTypePolicy.IsAllowed(CardType) - метод
Возвращает признак того, что выполнение методов расширения допустимо для
заданного типа файла.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsAllowed(
    	CardType fileType
    )
VB __Копировать
     Public Function IsAllowed ( 
    	fileType As CardType
    ) As Boolean
C++ __Копировать
     public:
    virtual bool IsAllowed(
    	CardType^ fileType
    ) sealed
F# __Копировать
     abstract IsAllowed : 
            fileType : CardType -> bool 
    override IsAllowed : 
            fileType : CardType -> bool 
#### Параметры
fileType [CardType](T_Tessa_Cards_CardType.htm)
    Тип файла, идентификатор или имя которого проверяются.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если выполнение методов расширения допустимо для заданного типа файла;
false в противном случае.
#### Реализации
[ICardFileTypePolicy.IsAllowed(CardType)](M_Tessa_Cards_Extensions_ICardFileTypePolicy_IsAllowed_1.htm)  
##  __См. также
#### Ссылки
[CardFileTypePolicy - ](T_Tessa_Cards_Extensions_CardFileTypePolicy.htm)
[IsAllowed -
перегрузка](Overload_Tessa_Cards_Extensions_CardFileTypePolicy_IsAllowed.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
