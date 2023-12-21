# CardSatelliteHelper.AddSatelliteToList - метод
Добавляет карточку-сателлит в список карточек-сателлитов, который должен
содержаться в пакете основной карточки. Если список не был создан, то он
автоматически создаётся при первом вызове метода.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void AddSatelliteToList(
    	Card mainCard,
    	Card satellite,
    	string satelliteKey
    )
VB __Копировать
     Public Shared Sub AddSatelliteToList ( 
    	mainCard As Card,
    	satellite As Card,
    	satelliteKey As String
    )
C++ __Копировать
     public:
    static void AddSatelliteToList(
    	Card^ mainCard, 
    	Card^ satellite, 
    	String^ satelliteKey
    )
F# __Копировать
     static member AddSatelliteToList : 
            mainCard : Card * 
            satellite : Card * 
            satelliteKey : string -> unit 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Пакет основной карточки, в которой содержится список карточек-сателлитов.
satellite [Card](T_Tessa_Cards_Card.htm)
     Карточка-сателлит, которая добавляется в список. При этом не выполняется автоматического клонирования структуры. Может быть равна null, тогда карточек не добавляется, но список карточек-сателлитов будет создан пустым, если он отсутствовал, что можно использовать как индикация того, что расширение выполнялось, но сателлиты отсутствуют. 
satelliteKey [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому список карточек-сателлитов содержится в основной карточке. Ключ должен быть уникален для списка 
## __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
