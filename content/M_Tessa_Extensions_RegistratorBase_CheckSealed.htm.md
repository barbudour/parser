# RegistratorBase.CheckSealed - метод
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected void CheckSealed()
VB __Копировать
     Protected Sub CheckSealed
C++ __Копировать
     protected:
    void CheckSealed()
F# __Копировать
     member CheckSealed : unit -> unit 
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[RegistratorBase - ](T_Tessa_Extensions_RegistratorBase.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
[Tessa.Platform.ObjectSealedException]
