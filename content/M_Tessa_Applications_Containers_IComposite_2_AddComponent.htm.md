# IComposite<TComponent, TOperation>.AddComponent - метод
Добавляет компонент component в контейнер. Добавляемый компонент должен быть
не равен null.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers](N_Tessa_Applications_Containers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    TComponent AddComponent(
    	[NotNullAttribute] TComponent component
    )
VB __Копировать
    <NotNullAttribute>
    Function AddComponent ( 
    	<NotNullAttribute> component As TComponent
    ) As TComponent
C++ __Копировать
    [NotNullAttribute]
    TComponent AddComponent(
    	[NotNullAttribute] TComponent component
    )
F# __Копировать
     [<NotNullAttribute>]
    abstract AddComponent : 
            [<NotNullAttribute>] component : 'TComponent -> 'TComponent 
#### Параметры
component [TComponent](T_Tessa_Applications_Containers_IComposite_2.htm)
     Добавляемый в контейнер компонент. 
#### Возвращаемое значение
[TComponent](T_Tessa_Applications_Containers_IComposite_2.htm)  
Возвращает добавленный в контейнер компонент
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
