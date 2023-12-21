# CommonHelper.GetHostGlobalName<T> \- метод
Возвращает глобально уникальное имя в пределах хоста для заданного типа.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetHostGlobalName<T>()
VB __Копировать
     Public Shared Function GetHostGlobalName(Of T) As String
C++ __Копировать
     public:
    generic<typename T>
    static String^ GetHostGlobalName()
F# __Копировать
     static member GetHostGlobalName : unit -> string 
#### Параметры типа
T
    Тип, для которого будет возвращено глобально уникальное имя.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Глобально уникальное имя в пределах хоста для заданного типа.
##  __Заметки
Глобально уникальное имя в пределах хоста включает имя типа и отображаемое имя
сборки, в которой он расположен.
## __См. также
#### Ссылки
[CommonHelper - ](T_Chronos_Platform_CommonHelper.htm)
[GetHostGlobalName -
перегрузка](Overload_Chronos_Platform_CommonHelper_GetHostGlobalName.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
