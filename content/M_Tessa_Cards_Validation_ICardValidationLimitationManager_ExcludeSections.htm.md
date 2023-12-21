# ICardValidationLimitationManager.ExcludeSections - метод
Исключает набор секций из доступных для валидатора. Если секция исключена из
проверки, то валидаторы по ней не выполняются.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ICardValidationLimitationManager ExcludeSections(
    	params string[] sectionNames
    )
VB __Копировать
     Function ExcludeSections ( 
    	ParamArray sectionNames As String()
    ) As ICardValidationLimitationManager
C++ __Копировать
    ICardValidationLimitationManager^ ExcludeSections(
    	... array<String^>^ sectionNames
    )
F# __Копировать
     abstract ExcludeSections : 
            sectionNames : string[] -> ICardValidationLimitationManager 
#### Параметры
sectionNames [String](https://learn.microsoft.com/dotnet/api/system.string)[]
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
