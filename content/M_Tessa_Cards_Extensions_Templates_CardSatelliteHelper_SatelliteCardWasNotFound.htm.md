# CardSatelliteHelper.SatelliteCardWasNotFound - метод
Возвращает признак того, что карточка-сателлит была установлена как
отсутствующая в пакете основной карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool SatelliteCardWasNotFound(
    	Card mainCard,
    	string satelliteKey
    )
VB __Копировать
     Public Shared Function SatelliteCardWasNotFound ( 
    	mainCard As Card,
    	satelliteKey As String
    ) As Boolean
C++ __Копировать
     public:
    static bool SatelliteCardWasNotFound(
    	Card^ mainCard, 
    	String^ satelliteKey
    )
F# __Копировать
     static member SatelliteCardWasNotFound : 
            mainCard : Card * 
            satelliteKey : string -> bool 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Пакет основной карточки, в которой может быть установлена карточка-сателлит.
satelliteKey [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ в [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm) основной карточки, который содержит хранилище карточки-сателлита, или null, если используется системный ключ по умолчанию (подходит для случаев, когда карточку сопровождает единственный сателлит). 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если карточка-сателлит была установлена как отсутствующая в пакете
основной карточки; false в противном случае.
## __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
