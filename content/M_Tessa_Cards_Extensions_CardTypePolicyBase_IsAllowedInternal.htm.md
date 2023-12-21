# CardTypePolicyBase.IsAllowedInternal(String) - метод
Возвращает признак того, что выполнение методов расширения допустимо для типа
карточки с заданным именем.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected bool IsAllowedInternal(
    	string cardTypeName
    )
VB __Копировать
     Protected Function IsAllowedInternal ( 
    	cardTypeName As String
    ) As Boolean
C++ __Копировать
     protected:
    bool IsAllowedInternal(
    	String^ cardTypeName
    )
F# __Копировать
     member IsAllowedInternal : 
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
[CardTypePolicyBase - ](T_Tessa_Cards_Extensions_CardTypePolicyBase.htm)
[IsAllowedInternal -
перегрузка](Overload_Tessa_Cards_Extensions_CardTypePolicyBase_IsAllowedInternal.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
