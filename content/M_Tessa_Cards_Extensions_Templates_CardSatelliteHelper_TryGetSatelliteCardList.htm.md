# CardSatelliteHelper.TryGetSatelliteCardList - метод
Возвращает список карточек-сателлитов, который был установлен в пакете
основной карточки, или null, если карточки-сателлиты не установлены, т.е.
список пустой.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<Card> TryGetSatelliteCardList(
    	Card mainCard,
    	string satelliteKey
    )
VB __Копировать
     Public Shared Function TryGetSatelliteCardList ( 
    	mainCard As Card,
    	satelliteKey As String
    ) As List(Of Card)
C++ __Копировать
     public:
    static List<Card^>^ TryGetSatelliteCardList(
    	Card^ mainCard, 
    	String^ satelliteKey
    )
F# __Копировать
     static member TryGetSatelliteCardList : 
            mainCard : Card * 
            satelliteKey : string -> List<Card> 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Пакет основной карточки, в которой может быть установлен список карточек-сателлитов.
satelliteKey [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому размещается список с карточками-сателлитами в Info основной карточке. Ключ должен быть уникален для списка. 
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Card](T_Tessa_Cards_Card.htm)>  
Список карточек-сателлитов, который был установлен в пакете основной карточки,
или null, если карточки-сателлиты не установлены, т.е. список пустой.
## __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
