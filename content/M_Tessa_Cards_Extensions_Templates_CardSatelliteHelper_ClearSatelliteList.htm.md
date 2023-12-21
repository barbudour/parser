# CardSatelliteHelper.ClearSatelliteList - метод
Очищает список карточек-сателлитов, если он существовал в пакете основной
карточки (но не удаляет пустой список из структуры).
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void ClearSatelliteList(
    	Card mainCard,
    	string satelliteKey
    )
VB __Копировать
     Public Shared Sub ClearSatelliteList ( 
    	mainCard As Card,
    	satelliteKey As String
    )
C++ __Копировать
     public:
    static void ClearSatelliteList(
    	Card^ mainCard, 
    	String^ satelliteKey
    )
F# __Копировать
     static member ClearSatelliteList : 
            mainCard : Card * 
            satelliteKey : string -> unit 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Пакет основной карточки, в которой может содержаться список карточек-сателлитов.
satelliteKey [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому список карточек-сателлитов содержится в основной карточке. Ключ должен быть уникален для списка 
## __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
