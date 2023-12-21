# AssemblySynchronizationSource.ProcessAssembly - метод
Устанавливает исполняемый файла приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IAssemblySynchronizationSource ProcessAssembly(
    	Assembly assembly
    )
VB __Копировать
     Public Function ProcessAssembly ( 
    	assembly As Assembly
    ) As IAssemblySynchronizationSource
C++ __Копировать
     public:
    virtual IAssemblySynchronizationSource^ ProcessAssembly(
    	Assembly^ assembly
    ) sealed
F# __Копировать
     abstract ProcessAssembly : 
            assembly : Assembly -> IAssemblySynchronizationSource 
    override ProcessAssembly : 
            assembly : Assembly -> IAssemblySynchronizationSource 
#### Параметры
assembly
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)
     Исполняемый файл приложения 
#### Возвращаемое значение
[IAssemblySynchronizationSource](T_Tessa_Applications_Synchronization_IAssemblySynchronizationSource.htm)  
Источник синхронизации
[AssemblySynchronizationSource](T_Tessa_Applications_Synchronization_AssemblySynchronizationSource.htm).
#### Реализации
[IAssemblySynchronizationSource.ProcessAssembly(Assembly)](M_Tessa_Applications_Synchronization_IAssemblySynchronizationSource_ProcessAssembly.htm)  
##  __См. также
#### Ссылки
[AssemblySynchronizationSource -
](T_Tessa_Applications_Synchronization_AssemblySynchronizationSource.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
