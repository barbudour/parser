# WeakEventHandler - делегат
##  __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate bool WeakEventHandler(
    	Type managerType,
    	Object sender,
    	EventArgs e
    )
VB __Копировать
     Public Delegate Function WeakEventHandler ( 
    	managerType As Type,
    	sender As Object,
    	e As EventArgs
    ) As Boolean
C++ __Копировать
     public delegate bool WeakEventHandler(
    	Type^ managerType, 
    	Object^ sender, 
    	EventArgs^ e
    )
F# __Копировать
     type WeakEventHandler = 
        delegate of 
            managerType : Type * 
            sender : Object * 
            e : EventArgs -> bool
#### Параметры
managerType [Type](https://learn.microsoft.com/dotnet/api/system.type)
sender [Object](https://learn.microsoft.com/dotnet/api/system.object)
e [EventArgs](https://learn.microsoft.com/dotnet/api/system.eventargs)
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
