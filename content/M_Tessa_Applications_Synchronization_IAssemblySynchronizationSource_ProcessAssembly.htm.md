# IAssemblySynchronizationSource.ProcessAssembly - метод
Устанавливает исполняемый файла приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    IAssemblySynchronizationSource ProcessAssembly(
    	[NotNullAttribute] Assembly assembly
    )
VB __Копировать
    <NotNullAttribute>
    Function ProcessAssembly ( 
    	<NotNullAttribute> assembly As Assembly
    ) As IAssemblySynchronizationSource
C++ __Копировать
    [NotNullAttribute]
    IAssemblySynchronizationSource^ ProcessAssembly(
    	[NotNullAttribute] Assembly^ assembly
    )
F# __Копировать
     [<NotNullAttribute>]
    abstract ProcessAssembly : 
            [<NotNullAttribute>] assembly : Assembly -> IAssemblySynchronizationSource 
#### Параметры
assembly
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)
     Исполняемый файл приложения 
#### Возвращаемое значение
[IAssemblySynchronizationSource](T_Tessa_Applications_Synchronization_IAssemblySynchronizationSource.htm)  
Источник синхронизации
[AssemblySynchronizationSource](T_Tessa_Applications_Synchronization_AssemblySynchronizationSource.htm).
## __См. также
#### Ссылки
[IAssemblySynchronizationSource -
](T_Tessa_Applications_Synchronization_IAssemblySynchronizationSource.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
