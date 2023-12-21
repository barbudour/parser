# LinuxChronosPlatformDependencies.CreateGlobalMutex - метод
Создаёт мьютекс по глобально уникальному имени, который можно использовать для
синхронизации процессов как минимум в пределах сессии пользователя и всех
процессов в ней.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform.Linux (в Chronos.Platform.Linux.dll) Версия:
3.6.0.17
C# __Копировать
     public override IGlobalMutex CreateGlobalMutex(
    	string name
    )
VB __Копировать
     Public Overrides Function CreateGlobalMutex ( 
    	name As String
    ) As IGlobalMutex
C++ __Копировать
     public:
    virtual IGlobalMutex^ CreateGlobalMutex(
    	String^ name
    ) override
F# __Копировать
     abstract CreateGlobalMutex : 
            name : string -> IGlobalMutex 
    override CreateGlobalMutex : 
            name : string -> IGlobalMutex 
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
     Глобально уникальное имя объекта синхронизации. Не должно быть равно null или пустой строке. Обычно не зависит от регистра символов. 
#### Возвращаемое значение
[IGlobalMutex](T_Chronos_Platform_IPC_IGlobalMutex.htm)  
Мьютекс, созданный по глобально уникальному имени. Не должен быть равен null.
#### Реализации
[IChronosPlatformDependencies.CreateGlobalMutex(String)](M_Chronos_Platform_IChronosPlatformDependencies_CreateGlobalMutex.htm)  
##  __См. также
#### Ссылки
[LinuxChronosPlatformDependencies -
](T_Chronos_Platform_LinuxChronosPlatformDependencies.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
