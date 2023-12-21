# ICardValidationLimitationManager.LimitRows - метод
Ограничивает набор строк, доступных в секции. Добавление ограничений по
строкам секции также добавляет ограничение на эту секцию, если она не была
добавлена.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ICardValidationLimitationManager LimitRows(
    	string sectionName,
    	params Guid[] rowIDs
    )
VB __Копировать
     Function LimitRows ( 
    	sectionName As String,
    	ParamArray rowIDs As Guid()
    ) As ICardValidationLimitationManager
C++ __Копировать
    ICardValidationLimitationManager^ LimitRows(
    	String^ sectionName, 
    	... array<Guid>^ rowIDs
    )
F# __Копировать
     abstract LimitRows : 
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
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[ICardValidationLimitationManager -
](T_Tessa_Cards_Validation_ICardValidationLimitationManager.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
[Tessa.Platform.ObjectSealedException]
