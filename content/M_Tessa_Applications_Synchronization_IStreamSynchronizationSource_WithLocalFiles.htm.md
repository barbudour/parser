# IStreamSynchronizationSource.WithLocalFiles - метод
Задаёт информацию о локальных файлах.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    IStreamSynchronizationSource WithLocalFiles(
    	[CanBeNullAttribute] LocalFileEntryCollection localFiles
    )
VB __Копировать
    <NotNullAttribute>
    Function WithLocalFiles ( 
    	<CanBeNullAttribute> localFiles As LocalFileEntryCollection
    ) As IStreamSynchronizationSource
C++ __Копировать
    [NotNullAttribute]
    IStreamSynchronizationSource^ WithLocalFiles(
    	[CanBeNullAttribute] LocalFileEntryCollection^ localFiles
    )
F# __Копировать
     [<NotNullAttribute>]
    abstract WithLocalFiles : 
            [<CanBeNullAttribute>] localFiles : LocalFileEntryCollection -> IStreamSynchronizationSource 
#### Параметры
localFiles
[LocalFileEntryCollection](T_Tessa_Applications_Synchronization_LocalFileEntryCollection.htm)
    Коллекция содержащая информацию о локальных файлах.
#### Возвращаемое значение
[IStreamSynchronizationSource](T_Tessa_Applications_Synchronization_IStreamSynchronizationSource.htm)  
Целевой объект синхронизации.
##  __См. также
#### Ссылки
[IStreamSynchronizationSource -
](T_Tessa_Applications_Synchronization_IStreamSynchronizationSource.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
