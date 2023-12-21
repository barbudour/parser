# AssemblyLoaderOptions.CheckInterface<T> \- метод
Указывает, что для указанного типа интерфейса потребуется проверить, реализуем
ли его экспортированный тип.
##  __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public IAssemblyLoaderOptions CheckInterface<T>()
    where T : class
VB __Копировать
     Public Function CheckInterface(Of T As Class) As IAssemblyLoaderOptions
C++ __Копировать
     public:
    generic<typename T>
    where T : ref class
    virtual IAssemblyLoaderOptions^ CheckInterface() sealed
F# __Копировать
     abstract CheckInterface : unit -> IAssemblyLoaderOptions  when 'T : not struct
    override CheckInterface : unit -> IAssemblyLoaderOptions  when 'T : not struct
#### Параметры типа
T
    Тип интерфейса, для которого будет выполняться проверка.
#### Возвращаемое значение
[IAssemblyLoaderOptions](T_Chronos_Platform_Composition_IAssemblyLoaderOptions.htm)  
Текущий объект для цепочки вызовов.
#### Реализации
[IAssemblyLoaderOptions.CheckInterface<T>()](M_Chronos_Platform_Composition_IAssemblyLoaderOptions_CheckInterface__1.htm)  
##  __См. также
#### Ссылки
[AssemblyLoaderOptions -
](T_Chronos_Platform_Composition_AssemblyLoaderOptions.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
