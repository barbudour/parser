# CardValidationLimitationManager.LimitRows - метод
Ограничивает набор строк, доступных в секции. Добавление ограничений по
строкам секции также добавляет ограничение на эту секцию, если она не была
добавлена.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardValidationLimitationManager LimitRows(
    	string sectionName,
    	params Guid[] rowIDs
    )
VB __Копировать
     Public Function LimitRows ( 
    	sectionName As String,
    	ParamArray rowIDs As Guid()
    ) As ICardValidationLimitationManager
C++ __Копировать
     public:
    virtual ICardValidationLimitationManager^ LimitRows(
    	String^ sectionName, 
    	... array<Guid>^ rowIDs
    ) sealed
F# __Копировать
     abstract LimitRows : 
            sectionName : string * 
            rowIDs : Guid[] -> ICardValidationLimitationManager 
    override LimitRows : 
            sectionName : string * 
            rowIDs : Guid[] -> ICardValidationLimitationManager 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции, для строк которой вводится ограничение.
rowIDs [Guid](https://learn.microsoft.com/dotnet/api/system.guid)[]
    Идентификаторы строк.
#### Возвращаемое значение
[ICardValidationLimitationManager](T_Tessa_Cards_Validation_ICardValidationLimitationManager.htm)  
Текущий объект для цепочки вызовов.
#### Реализации
[ICardValidationLimitationManager.LimitRows(String,
Guid[])](M_Tessa_Cards_Validation_ICardValidationLimitationManager_LimitRows.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardValidationLimitationManager -
](T_Tessa_Cards_Validation_CardValidationLimitationManager.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
[Tessa.Platform.ObjectSealedException]
