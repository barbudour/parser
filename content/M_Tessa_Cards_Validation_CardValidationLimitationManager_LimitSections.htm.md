# CardValidationLimitationManager.LimitSections - метод
Ограничивает набор секций, доступных для валидатора. Если ограничение секций
не выполнялось, то валидация выполняется по всем секциям, иначе только по
заданным. Указание коллекционной секции не означает автоматически возможность
редактировать любые строки этой секции.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardValidationLimitationManager LimitSections(
    	params string[] sectionNames
    )
VB __Копировать
     Public Function LimitSections ( 
    	ParamArray sectionNames As String()
    ) As ICardValidationLimitationManager
C++ __Копировать
     public:
    virtual ICardValidationLimitationManager^ LimitSections(
    	... array<String^>^ sectionNames
    ) sealed
F# __Копировать
     abstract LimitSections : 
            sectionNames : string[] -> ICardValidationLimitationManager 
    override LimitSections : 
            sectionNames : string[] -> ICardValidationLimitationManager 
#### Параметры
sectionNames [String](https://learn.microsoft.com/dotnet/api/system.string)[]
    Имена секций, для которых вводится ограничение.
#### Возвращаемое значение
[ICardValidationLimitationManager](T_Tessa_Cards_Validation_ICardValidationLimitationManager.htm)  
Текущий объект для цепочки вызовов.
#### Реализации
[ICardValidationLimitationManager.LimitSections(String[])](M_Tessa_Cards_Validation_ICardValidationLimitationManager_LimitSections.htm)  
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
