# ContainerInitializationDelegate - делегат
Осуществляет инициализацию контейнера
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate void ContainerInitializationDelegate(
    	[NotNullAttribute] IUnityContainer container
    )
VB __Копировать
     Public Delegate Sub ContainerInitializationDelegate ( 
    	<NotNullAttribute> container As IUnityContainer
    )
C++ __Копировать
     public delegate void ContainerInitializationDelegate(
    	[NotNullAttribute] IUnityContainer^ container
    )
F# __Копировать
     type ContainerInitializationDelegate = 
        delegate of 
            [<NotNullAttribute>] container : IUnityContainer -> unit
#### Параметры
container IUnityContainer
     Инициализируемый контейнер 
## __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
