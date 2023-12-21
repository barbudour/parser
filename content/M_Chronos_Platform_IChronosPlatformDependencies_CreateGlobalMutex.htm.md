# IChronosPlatformDependencies.CreateGlobalMutex - метод
Создаёт мьютекс по глобально уникальному имени, который можно использовать для
синхронизации процессов как минимум в пределах сессии пользователя и всех
процессов в ней.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     IGlobalMutex CreateGlobalMutex(
    	string name
    )
VB __Копировать
     Function CreateGlobalMutex ( 
    	name As String
    ) As IGlobalMutex
C++ __Копировать
    IGlobalMutex^ CreateGlobalMutex(
    	String^ name
    )
F# __Копировать
     abstract CreateGlobalMutex : 
            name : string -> IGlobalMutex 
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
     Глобально уникальное имя объекта синхронизации. Не должно быть равно null или пустой строке. Обычно не зависит от регистра символов. 
#### Возвращаемое значение
[IGlobalMutex](T_Chronos_Platform_IPC_IGlobalMutex.htm)  
Мьютекс, созданный по глобально уникальному имени. Не должен быть равен null.
## __См. также
#### Ссылки
[IChronosPlatformDependencies -
](T_Chronos_Platform_IChronosPlatformDependencies.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
