# CardValidationLimitationManager.ExcludeColumns - метод
Исключает набор колонок для указанной секции из доступных для валидатора. Если
колонка исключена из проверки, то валидаторы по ней не выполняются.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardValidationLimitationManager ExcludeColumns(
    	string sectionName,
    	params string[] columnNames
    )
VB __Копировать
     Public Function ExcludeColumns ( 
    	sectionName As String,
    	ParamArray columnNames As String()
    ) As ICardValidationLimitationManager
C++ __Копировать
     public:
    virtual ICardValidationLimitationManager^ ExcludeColumns(
    	String^ sectionName, 
    	... array<String^>^ columnNames
    ) sealed
F# __Копировать
     abstract ExcludeColumns : 
            sectionName : string * 
            columnNames : string[] -> ICardValidationLimitationManager 
    override ExcludeColumns : 
            sectionName : string * 
            columnNames : string[] -> ICardValidationLimitationManager 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции, колонки которой исключаются из проверки.
columnNames [String](https://learn.microsoft.com/dotnet/api/system.string)[]
    Имена колонок, которые исключаются из проверки.
#### Возвращаемое значение
[ICardValidationLimitationManager](T_Tessa_Cards_Validation_ICardValidationLimitationManager.htm)  
Текущий объект для цепочки вызовов.
#### Реализации
[ICardValidationLimitationManager.ExcludeColumns(String,
String[])](M_Tessa_Cards_Validation_ICardValidationLimitationManager_ExcludeColumns.htm)  
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
