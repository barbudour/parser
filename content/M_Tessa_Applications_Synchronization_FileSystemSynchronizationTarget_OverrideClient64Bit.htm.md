# FileSystemSynchronizationTarget.OverrideClient64Bit - метод
Переопределяет свойство Client64Bit для пакета приложения, создаваемого из
папки.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IFileSystemSynchronizationTarget OverrideClient64Bit(
    	bool? client64Bit
    )
VB __Копировать
     Public Function OverrideClient64Bit ( 
    	client64Bit As Boolean?
    ) As IFileSystemSynchronizationTarget
C++ __Копировать
     public:
    virtual IFileSystemSynchronizationTarget^ OverrideClient64Bit(
    	Nullable<bool> client64Bit
    ) sealed
F# __Копировать
     abstract OverrideClient64Bit : 
            client64Bit : Nullable<bool> -> IFileSystemSynchronizationTarget 
    override OverrideClient64Bit : 
            client64Bit : Nullable<bool> -> IFileSystemSynchronizationTarget 
#### Параметры
client64Bit
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
     Признак Client64Bit, переопределяемый для пакета приложения, создаваемого из папки, или null, если переопределение не требуется. 
#### Возвращаемое значение
[IFileSystemSynchronizationTarget](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationTarget.htm)  
Целевой объект синхронизации.
#### Реализации
[IFileSystemSynchronizationTarget.OverrideClient64Bit(Nullable<Boolean>)](M_Tessa_Applications_Synchronization_IFileSystemSynchronizationTarget_OverrideClient64Bit.htm)  
##  __См. также
#### Ссылки
[FileSystemSynchronizationTarget -
](T_Tessa_Applications_Synchronization_FileSystemSynchronizationTarget.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
