# CardSatelliteHelper.CreateSatelliteInfo - метод
Создаёт объект
[SatelliteInfo](T_Tessa_Cards_Extensions_Templates_SatelliteInfo.htm),
содержащий информацию по карточке-сателлиту для задания.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static SatelliteInfo CreateSatelliteInfo(
    	Card satelliteCard,
    	string sectionName,
    	string taskRowIDFieldName
    )
VB __Копировать
     Public Shared Function CreateSatelliteInfo ( 
    	satelliteCard As Card,
    	sectionName As String,
    	taskRowIDFieldName As String
    ) As SatelliteInfo
C++ __Копировать
     public:
    static SatelliteInfo^ CreateSatelliteInfo(
    	Card^ satelliteCard, 
    	String^ sectionName, 
    	String^ taskRowIDFieldName
    )
F# __Копировать
     static member CreateSatelliteInfo : 
            satelliteCard : Card * 
            sectionName : string * 
            taskRowIDFieldName : string -> SatelliteInfo 
#### Параметры
satelliteCard [Card](T_Tessa_Cards_Card.htm)
    Карточка-сателлит для задания, для которой требуется создать объект.
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции в карточке-сателлите, в которой содержится поле с идентификатором задания.
taskRowIDFieldName
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя поля из секции sectionName, в котором содержится идентификатор задания.
#### Возвращаемое значение
[SatelliteInfo](T_Tessa_Cards_Extensions_Templates_SatelliteInfo.htm)  
Объект [SatelliteInfo](T_Tessa_Cards_Extensions_Templates_SatelliteInfo.htm),
содержащий информацию по карточке-сателлиту для задания.
##  __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
