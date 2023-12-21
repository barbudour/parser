# CardSatelliteHelper.SetSatellite - метод
Сохраняет карточку-сателлит в пакете основной карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetSatellite(
    	Card mainCard,
    	Card satellite,
    	string satelliteKey
    )
VB __Копировать
     Public Shared Sub SetSatellite ( 
    	mainCard As Card,
    	satellite As Card,
    	satelliteKey As String
    )
C++ __Копировать
     public:
    static void SetSatellite(
    	Card^ mainCard, 
    	Card^ satellite, 
    	String^ satelliteKey
    )
F# __Копировать
     static member SetSatellite : 
            mainCard : Card * 
            satellite : Card * 
            satelliteKey : string -> unit 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Пакет основной карточки.
satellite [Card](T_Tessa_Cards_Card.htm)
    Карточка-сателлит или null, если карточка-сателлит ещё не создана.
satelliteKey [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ в [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm) основной карточки, который содержит хранилище карточки-сателлита, или null, если используется системный ключ по умолчанию (подходит для случаев, когда карточку сопровождает единственный сателлит). 
## __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
