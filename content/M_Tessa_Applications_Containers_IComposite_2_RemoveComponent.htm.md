# IComposite<TComponent, TOperation>.RemoveComponent - метод
Удаляет компонент component из контейнера. Удаляемый компонент должен быть не
равен null
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers](N_Tessa_Applications_Containers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void RemoveComponent(
    	[NotNullAttribute] TComponent component
    )
VB __Копировать
     Sub RemoveComponent ( 
    	<NotNullAttribute> component As TComponent
    )
C++ __Копировать
     void RemoveComponent(
    	[NotNullAttribute] TComponent component
    )
F# __Копировать
     abstract RemoveComponent : 
            [<NotNullAttribute>] component : 'TComponent -> unit 
#### Параметры
component [TComponent](T_Tessa_Applications_Containers_IComposite_2.htm)
     Удаляемый из контейнера компонент 
## __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Компонент component равен null  
---|---  
## __См. также
#### Ссылки
[IComposite<TComponent, TOperation> \-
](T_Tessa_Applications_Containers_IComposite_2.htm)
[Tessa.Applications.Containers - пространство
имён](N_Tessa_Applications_Containers.htm)
