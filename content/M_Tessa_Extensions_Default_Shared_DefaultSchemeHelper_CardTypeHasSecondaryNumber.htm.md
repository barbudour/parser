# DefaultSchemeHelper.CardTypeHasSecondaryNumber - метод
Возвращает признак того, что в схеме типа карточки присутствуют все поля с
Secondary-номером.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared](N_Tessa_Extensions_Default_Shared.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool CardTypeHasSecondaryNumber(
    	CardType cardType
    )
VB __Копировать
     Public Shared Function CardTypeHasSecondaryNumber ( 
    	cardType As CardType
    ) As Boolean
C++ __Копировать
     public:
    static bool CardTypeHasSecondaryNumber(
    	CardType^ cardType
    )
F# __Копировать
     static member CardTypeHasSecondaryNumber : 
            cardType : CardType -> bool 
#### Параметры
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточки, схему которого требуется проверить.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если в схеме типа карточки присутствуют все поля с Secondary-номером;
false в противном случае.
## __См. также
#### Ссылки
[DefaultSchemeHelper -
](T_Tessa_Extensions_Default_Shared_DefaultSchemeHelper.htm)
[Tessa.Extensions.Default.Shared - пространство
имён](N_Tessa_Extensions_Default_Shared.htm)
