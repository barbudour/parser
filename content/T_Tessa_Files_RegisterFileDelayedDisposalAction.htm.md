# RegisterFileDelayedDisposalAction - делегат
Функция регистрации отложенного удаления содержимого (удаления временного
файла), которое невозможно выполнить сразу же.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate void RegisterFileDelayedDisposalAction(
    	Func<bool> disposeContentFunc
    )
VB __Копировать
     Public Delegate Sub RegisterFileDelayedDisposalAction ( 
    	disposeContentFunc As Func(Of Boolean)
    )
C++ __Копировать
     public delegate void RegisterFileDelayedDisposalAction(
    	Func<bool>^ disposeContentFunc
    )
F# __Копировать
     type RegisterFileDelayedDisposalAction = 
        delegate of 
            disposeContentFunc : Func<bool> -> unit
#### Параметры
disposeContentFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
     Функция, выполняющая отложенное удаление содержимого. Не равна null. Функция удаляет содержимое и возвращает признак того, что удаление успешно выполнено. Успешность функции не должна зависеть от того, был ли освобождён соответствующий объект [IFileContent](T_Tessa_Files_IFileContent.htm) вызовом Dispose(). 
## __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
