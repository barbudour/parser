# CardSchemeSerializableObject.RepairAsync(ICardSchemeInfoProvider,
CancellationToken) - метод
Метод восстанавливает объект к работоспособному состоянии в соответствии со
схемой. Этот процесс включает удаление данных из текущего объекта, которые
имеют отношение к схеме, но фактически в ней отсутствуют.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<ValidationResult> RepairAsync(
    	ICardSchemeInfoProvider cardSchemeInfoProvider,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function RepairAsync ( 
    	cardSchemeInfoProvider As ICardSchemeInfoProvider,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ValidationResult)
C++ __Копировать
     public:
    ValueTask<ValidationResult^> RepairAsync(
    	ICardSchemeInfoProvider^ cardSchemeInfoProvider, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member RepairAsync : 
            cardSchemeInfoProvider : ICardSchemeInfoProvider * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValidationResult> 
#### Параметры
cardSchemeInfoProvider
[ICardSchemeInfoProvider](T_Tessa_Cards_ICardSchemeInfoProvider.htm)
    Объект, предоставляющий информацию об актуальном состоянии схемы.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Результат валидации, в котором отражена информация об отсутствующих в схеме
объектах, которые были удалены из текущего объекта и всех его дочерних
объектов.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardSchemeSerializableObject -
](T_Tessa_Cards_CardSchemeSerializableObject.htm)
[RepairAsync -
перегрузка](Overload_Tessa_Cards_CardSchemeSerializableObject_RepairAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
