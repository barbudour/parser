# CommonHelper.GetGlobalName<T> \- метод
Возвращает глобально уникальное имя для заданного типа.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetGlobalName<T>()
VB __Копировать
     Public Shared Function GetGlobalName(Of T) As String
C++ __Копировать
     public:
    generic<typename T>
    static String^ GetGlobalName()
F# __Копировать
     static member GetGlobalName : unit -> string 
#### Параметры типа
T
    Тип, для которого будет возвращено глобально уникальное имя.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Глобально уникальное имя для заданного типа.
##  __Заметки
Глобально уникальное имя включает имя типа, местоположение сборки с типом и
заданное локальное имя.
## __См. также
#### Ссылки
[CommonHelper - ](T_Chronos_Platform_CommonHelper.htm)
[GetGlobalName -
перегрузка](Overload_Chronos_Platform_CommonHelper_GetGlobalName.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
