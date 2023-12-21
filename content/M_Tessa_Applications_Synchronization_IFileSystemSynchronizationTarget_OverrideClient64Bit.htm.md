# IFileSystemSynchronizationTarget.OverrideClient64Bit - метод
Переопределяет свойство Client64Bit для пакета приложения, создаваемого из
папки.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    IFileSystemSynchronizationTarget OverrideClient64Bit(
    	bool? client64Bit
    )
VB __Копировать
    <NotNullAttribute>
    Function OverrideClient64Bit ( 
    	client64Bit As Boolean?
    ) As IFileSystemSynchronizationTarget
C++ __Копировать
    [NotNullAttribute]
    IFileSystemSynchronizationTarget^ OverrideClient64Bit(
    	Nullable<bool> client64Bit
    )
F# __Копировать
     [<NotNullAttribute>]
    abstract OverrideClient64Bit : 
            client64Bit : Nullable<bool> -> IFileSystemSynchronizationTarget 
#### Параметры
client64Bit
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
     Признак Client64Bit, переопределяемый для пакета приложения, создаваемого из папки, или null, если переопределение не требуется. 
#### Возвращаемое значение
[IFileSystemSynchronizationTarget](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationTarget.htm)  
Целевой объект синхронизации.
##  __См. также
#### Ссылки
[IFileSystemSynchronizationTarget -
](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationTarget.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
