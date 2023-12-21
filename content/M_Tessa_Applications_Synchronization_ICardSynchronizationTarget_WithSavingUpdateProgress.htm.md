# ICardSynchronizationTarget.WithSavingUpdateProgress - метод
Устанавливает функцию обновления прогресса сохранения данных в карточку
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    ICardSynchronizationTarget WithSavingUpdateProgress(
    	[NotNullAttribute] Action<string> updateProgress
    )
VB __Копировать
    <NotNullAttribute>
    Function WithSavingUpdateProgress ( 
    	<NotNullAttribute> updateProgress As Action(Of String)
    ) As ICardSynchronizationTarget
C++ __Копировать
    [NotNullAttribute]
    ICardSynchronizationTarget^ WithSavingUpdateProgress(
    	[NotNullAttribute] Action<String^>^ updateProgress
    )
F# __Копировать
     [<NotNullAttribute>]
    abstract WithSavingUpdateProgress : 
            [<NotNullAttribute>] updateProgress : Action<string> -> ICardSynchronizationTarget 
#### Параметры
updateProgress
[Action](https://learn.microsoft.com/dotnet/api/system.action-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
     Прогресс обновления 
#### Возвращаемое значение
[ICardSynchronizationTarget](T_Tessa_Applications_Synchronization_ICardSynchronizationTarget.htm)  
Целевой объект
[ICardSynchronizationTarget](T_Tessa_Applications_Synchronization_ICardSynchronizationTarget.htm)
##  __См. также
#### Ссылки
[ICardSynchronizationTarget -
](T_Tessa_Applications_Synchronization_ICardSynchronizationTarget.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
