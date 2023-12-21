# CommonHelper.ObjectIsNull - метод
Возвращает true, если ссылка на объект равна null.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool ObjectIsNull(
    	Object obj
    )
VB __Копировать
     Public Shared Function ObjectIsNull ( 
    	obj As Object
    ) As Boolean
C++ __Копировать
     public:
    static bool ObjectIsNull(
    	Object^ obj
    )
F# __Копировать
     static member ObjectIsNull : 
            obj : Object -> bool 
#### Параметры
obj [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Ссылка на объект.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если ссылка на объект obj равна null; false в противном случае.
##  __Заметки
Метод можно использовать в LINQ для фильтрации ссылочных перечислений.
## __См. также
#### Ссылки
[CommonHelper - ](T_Chronos_Platform_CommonHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
