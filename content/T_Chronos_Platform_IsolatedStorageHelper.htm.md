# IsolatedStorageHelper - класс
Хэлперы по работе с изолированным хранилищем.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static class IsolatedStorageHelper
VB __Копировать
     Public NotInheritable Class IsolatedStorageHelper
C++ __Копировать
     public ref class IsolatedStorageHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type IsolatedStorageHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ IsolatedStorageHelper
##  __Методы
[DeleteFileForApplication](M_Chronos_Platform_IsolatedStorageHelper_DeleteFileForApplication.htm)|
Удаляет файл с заданным именем из хранилища, изолированного для пользователя и
сборки.  
---|---  
[ExceptionTypeIsExpected](M_Chronos_Platform_IsolatedStorageHelper_ExceptionTypeIsExpected.htm)|
Возвращает признак того, что указанное исключение принадлежит к одному из
типов исключений, которые могут быть созданы любым из методов класса
IsolatedStorageHelper, кроме этого метода.  
[ReadAllTextForApplicationAsync](M_Chronos_Platform_IsolatedStorageHelper_ReadAllTextForApplicationAsync.htm)|
Считывает весь текст из текстового файла с заданными именем, расположенного в
хранилище, изолированном для пользователя и сборки.  
[WriteAllTextForApplicationAsync](M_Chronos_Platform_IsolatedStorageHelper_WriteAllTextForApplicationAsync.htm)|
Записывает весь текст в текстовый файл с заданным именем, расположенный в
хранилище, изолированном для пользователя и сборки.  
## __См. также
#### Ссылки
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
