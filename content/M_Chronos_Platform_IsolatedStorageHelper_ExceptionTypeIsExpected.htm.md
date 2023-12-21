# IsolatedStorageHelper.ExceptionTypeIsExpected - метод
Возвращает признак того, что указанное исключение принадлежит к одному из
типов исключений, которые могут быть созданы любым из методов класса
[IsolatedStorageHelper](T_Chronos_Platform_IsolatedStorageHelper.htm), кроме
этого метода.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool ExceptionTypeIsExpected(
    	Exception ex
    )
VB __Копировать
     Public Shared Function ExceptionTypeIsExpected ( 
    	ex As Exception
    ) As Boolean
C++ __Копировать
     public:
    static bool ExceptionTypeIsExpected(
    	Exception^ ex
    )
F# __Копировать
     static member ExceptionTypeIsExpected : 
            ex : Exception -> bool 
#### Параметры
ex [Exception](https://learn.microsoft.com/dotnet/api/system.exception)
    Исключение, тип которого требуется проверить.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если исключение принадлежит к одному из типов исключений, которые могут
быть созданы любым из методов класса
[IsolatedStorageHelper](T_Chronos_Platform_IsolatedStorageHelper.htm), кроме
этого метода; false в противном случае.
##  __См. также
#### Ссылки
[IsolatedStorageHelper - ](T_Chronos_Platform_IsolatedStorageHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
