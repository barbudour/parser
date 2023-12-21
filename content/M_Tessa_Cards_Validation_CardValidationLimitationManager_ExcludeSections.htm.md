# CardValidationLimitationManager.ExcludeSections - метод
Исключает набор колонок для указанной секции из доступных для валидатора. Если
колонка исключена из проверки, то валидаторы по ней не выполняются.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardValidationLimitationManager ExcludeSections(
    	params string[] sectionNames
    )
VB __Копировать
     Public Function ExcludeSections ( 
    	ParamArray sectionNames As String()
    ) As ICardValidationLimitationManager
C++ __Копировать
     public:
    virtual ICardValidationLimitationManager^ ExcludeSections(
    	... array<String^>^ sectionNames
    ) sealed
F# __Копировать
     abstract ExcludeSections : 
            sectionNames : string[] -> ICardValidationLimitationManager 
    override ExcludeSections : 
            sectionNames : string[] -> ICardValidationLimitationManager 
#### Параметры
sectionNames [String](https://learn.microsoft.com/dotnet/api/system.string)[]
#### Возвращаемое значение
[ICardValidationLimitationManager](T_Tessa_Cards_Validation_ICardValidationLimitationManager.htm)  
Текущий объект для цепочки вызовов.
#### Реализации
[ICardValidationLimitationManager.ExcludeSections(String[])](M_Tessa_Cards_Validation_ICardValidationLimitationManager_ExcludeSections.htm)  
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
