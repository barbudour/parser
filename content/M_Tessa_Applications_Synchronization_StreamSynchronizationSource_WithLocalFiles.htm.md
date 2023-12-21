# StreamSynchronizationSource.WithLocalFiles - метод
Задаёт информацию о локальных файлах.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IStreamSynchronizationSource WithLocalFiles(
    	LocalFileEntryCollection localFiles
    )
VB __Копировать
     Public Function WithLocalFiles ( 
    	localFiles As LocalFileEntryCollection
    ) As IStreamSynchronizationSource
C++ __Копировать
     public:
    virtual IStreamSynchronizationSource^ WithLocalFiles(
    	LocalFileEntryCollection^ localFiles
    ) sealed
F# __Копировать
     abstract WithLocalFiles : 
            localFiles : LocalFileEntryCollection -> IStreamSynchronizationSource 
    override WithLocalFiles : 
            localFiles : LocalFileEntryCollection -> IStreamSynchronizationSource 
#### Параметры
localFiles
[LocalFileEntryCollection](T_Tessa_Applications_Synchronization_LocalFileEntryCollection.htm)
    Коллекция содержащая информацию о локальных файлах.
#### Возвращаемое значение
[IStreamSynchronizationSource](T_Tessa_Applications_Synchronization_IStreamSynchronizationSource.htm)  
Целевой объект синхронизации.
#### Реализации
[IStreamSynchronizationSource.WithLocalFiles(LocalFileEntryCollection)](M_Tessa_Applications_Synchronization_IStreamSynchronizationSource_WithLocalFiles.htm)  
##  __См. также
#### Ссылки
[StreamSynchronizationSource -
](T_Tessa_Applications_Synchronization_StreamSynchronizationSource.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
